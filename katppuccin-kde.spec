%global _basename katppuccin-kde

Name:           %{_basename}-colors
Version:        0.2.8

%global forgeurl https://github.com/hazel-bunny/%{name}
%global tag %{version}
%global date 20260406
%forgemeta

Release:        0%{?dist}
Summary:        🌻 Soothing pastel theme for KDE, with higher contrast and readability
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  sed

Requires:       %{name}-latte
Requires:       %{name}-frappe
Requires:       %{name}-macchiato
Requires:       %{name}-mocha

Recommends:     catppuccin-cursors

%description
%{summary}.

%files
%license LICENSE
%doc README.md

#--------------------------------------------------------------------------------------------------

%package        latte
Summary:        🌻 Soothing pastel theme for KDE, with higher contrast and readability
Requires:       %{_basename}-colors
Enhances:       %{_basename}-colors

%description    latte
%{summary}.

This package contains the latte colors.

%files          latte
%{_kf6_datadir}/color-schemes/KatppuccinLatte*.colors

#--------------------------------------------------------------------------------------------------

%package        frappe
Summary:        🌻 Soothing pastel theme for KDE, with higher contrast and readability
Requires:       %{_basename}-colors
Enhances:       %{_basename}-colors

%description    frappe
%{summary}.

This package contains the frappe colors.

%files          frappe
%{_kf6_datadir}/color-schemes/KatppuccinFrappe*.colors

#--------------------------------------------------------------------------------------------------

%package        macchiato
Summary:        🌻 Soothing pastel theme for KDE, with higher contrast and readability
Requires:       %{_basename}-colors
Enhances:       %{_basename}-colors

%description    macchiato
%{summary}.

This package contains the macchiato colors.

%files          macchiato
%{_kf6_datadir}/color-schemes/KatppuccinMacchiato*.colors

#--------------------------------------------------------------------------------------------------

%package        mocha
Summary:        🌻 Soothing pastel theme for KDE, with higher contrast and readability
Requires:       %{_basename}-colors
Enhances:       %{_basename}-colors

%description    mocha
%{summary}.

This package contains the mocha colors.

%files          mocha
%{_kf6_datadir}/color-schemes/KatppuccinMocha*.colors

#---------------------------------------------------------------------------------------------------

%prep
%forgeautosetup -p1
sed -i 's/sleep 2/sleep 0.2/' install.sh
sed -i 's/sleep 1/sleep 0.1/' install.sh
sed -i 's/mkdir -p "$COLORDIR" "$AURORAEDIR" "$LOOKANDFEELDIR" "$CURSORDIR"/\n/' CMakeLists.txt

%build
#nothing

%install
for f in {1..4}; do
    for c in {1..14}; do
        # for d in {1..2}; do
            bash ./install.sh ${f} ${c} 1 color
        # done
    done
done

mv dist/Katppuccin*.colors %{buildroot}%{_datadir}/color-schemes/

#---------------------------------------------------------------------------------------------------

%changelog
* Sat Apr 4 2026 Hazel Bunny <hazel_bunny@disroot.org> - 0.2.8-0
- Intial snapshot
